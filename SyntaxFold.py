import sublime, sublime_plugin, os, shutil, string

def plugin_loaded():
    if not os.path.exists(sublime.packages_path()+"/User/syntax_fold.sublime-settings"):
        print(sublime.packages_path())
        shutil.copyfile(sublime.packages_path()+"/SyntaxFold/syntax_fold.sublime-settings", sublime.packages_path()+"/User/syntax_fold.sublime-settings")


def get_source_scope(view):
    all_scopes = view.scope_name(view.sel()[0].begin())
    split_scopes = all_scopes.split(" ")
    for scope in split_scopes:
        if -1 != scope.find("source."):
            return scope
    return None

def get_markers(view):
    source_scope = get_source_scope(view)
    settings = sublime.load_settings('syntax_fold.sublime-settings')
    configs = settings.get('config')
    for config_object in configs:
        config_scope = config_object.get('scope', '')
        #allow for comma seperated source specifications
        if source_scope in config_scope:
            if 'startMarker' in config_object:
                if 'endMarker' in config_object:
                    return config_object['startMarker'], config_object['endMarker']
                else:
                    return config_object['startMarker'], None
    return None, None

def get_all_positions(view):

    start_marker, end_marker = get_markers(view)
    if None == start_marker:
        print('SyntaxFold: At least start marker must be specified. Aborting request.')
        return None, None

    start_positions = []
    end_positions = []

    #fill start positions
    start_markers = view.find_all(start_marker)
    for marker in start_markers:
        start_positions.append(view.line(marker.end()).end())

    #fill end positions
    if None != end_marker:
        end_markers = view.find_all(end_marker)
        for marker in end_markers:
            end_positions.append(view.line(marker.begin()).begin()-1)

    #If no end marker specified, utilize the next start marker as the end position
    else:
        for x in range(0, len(start_positions)-1):
            end_positions.append(view.line(start_positions[x+1]).begin()-1)

    end_positions_len = len(end_positions)
    start_positions_len = len(start_positions)

    if 0 == start_positions_len and 0 == end_positions_len:
        print('SyntaxFold: No start markers or end markers found in file. Aborting request.')
        return None, None

    return start_positions, end_positions

def get_all_fold_regions(view):

    start_positions, end_positions = get_all_positions(view)

    regions = []
    last_matched_end_pos = -1
    for end_pos in end_positions:
        last_matched_start_pos = -1
        for start_pos in start_positions:

            #if the start pos is beyond the position of
            #the end pos it isn't a match
            if start_pos > end_pos:
                break;

            #The start pos must be greater or equal to then the last matched end post
            #when matching
            elif start_pos > last_matched_end_pos:
                last_matched_start_pos = start_pos

        if (-1 != last_matched_start_pos):
            start_pos_match_position = view.line(last_matched_start_pos-1).begin()
            end_pos_match_position = view.line(end_pos+1).end()
            last_matched_end_pos = end_pos
            regions.append((last_matched_start_pos, end_pos, start_pos_match_position, end_pos_match_position))


    if 0 == len(regions):
        return None

    return regions

def operation_on_all_regions(fold_regions, operation):

    regions = []
    for fold_region in fold_regions:
        regions.append(sublime.Region(fold_region[0], fold_region[1]))

    operation(regions)

def operation_on_selected_region(view, fold_regions, operation):

    selection = view.sel()[0]

    for fold_region in fold_regions:
        if (fold_region[2] <= selection.begin()) and (fold_region[3] >= selection.end()):
            content = [sublime.Region(fold_region[0], fold_region[1])]
            operation(content)
            break;

#
#Operations
#
class FoldCommands(sublime_plugin.TextCommand):

    def fold(self, regions):
        if len(regions) > 0:
            self.view.fold(regions)

    def unfold(self, regions):
        if len(regions) > 0:
            self.view.unfold(regions)

class FoldAllCommand(FoldCommands):
    def run(self, edit):
        fold_regions = get_all_fold_regions(self.view)
        if (None == fold_regions):
            return;

        operation_on_all_regions(fold_regions, self.fold)

class UnfoldAllCommand(FoldCommands):
    def run(self, edit):
        fold_regions = get_all_fold_regions(self.view)
        if (None == fold_regions):
            return;

        operation_on_all_regions(fold_regions, self.unfold)

class FoldCurrentCommand(FoldCommands):
    def run(self, edit):
        fold_regions = get_all_fold_regions(self.view)
        if (None == fold_regions):
            return;

        operation_on_selected_region(self.view, fold_regions, self.fold)

class UnfoldCurrentCommand(FoldCommands):
    def run(self, edit):
        fold_regions = get_all_fold_regions(self.view)
        if (None == fold_regions):
            return;

        operation_on_selected_region(self.view, fold_regions, self.unfold)
