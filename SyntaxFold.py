import sublime, sublime_plugin, os, shutil

def plugin_loaded():
    if not os.path.exists(sublime.packages_path()+"\\User\\syntax_fold.sublime-settings"):
        print(sublime.packages_path())
        shutil.copyfile(sublime.packages_path()+"\\SyntaxFold\\syntax_fold.sublime-settings", sublime.packages_path()+"\\User\\syntax_fold.sublime-settings")



class FoldPanelCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.panel_cache = []
        self.config_map = {}
        s = sublime.load_settings('syntax_fold.sublime-settings')
        configs = s.get("config")
        for conf in configs:
            c=dict()
            c['startMarker']=conf.get('startMarker')
            c['endMarker']=conf.get('endMarker')
            if conf['name']=="Default":
                descr=startMarker
            else:
                descr=str(conf.get('startMarker'))
            self.panel_cache.append(["Set Default: "+conf['name'], descr ])
            self.config_map[conf['name']]=c
        self.panel_cache.append(["Add Another", "edit config to add another lang" ])
        self.view.window().show_quick_panel(self.panel_cache, self.on_select)

    def on_select(self, index):
        if index == -1:
            return
        name = self.panel_cache[index][0].replace("Set Default: ","")
        if name =="Add Another":           
            self.view.window().open_file(sublime.packages_path()+"\\User\\syntax_fold.sublime-settings")
        else:
            s = sublime.load_settings('syntax_fold.sublime-settings')
            config=s.get("config")
            newdef=config[index]
            newdef['name']="Default"
            s.set("default",newdef)
            sublime.save_settings("syntax_fold.sublime-settings")

class FoldAllCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        s = sublime.load_settings('syntax_fold.sublime-settings')
        config=s.get('default')
        startMarker = config.get("startMarker")
        endMarker = config.get("endMarker")
        startpos = self.view.find_all(startMarker)
        endpos=[]
        if endMarker==None:
            temp=[]
            for x in range(len(startpos)):
                temp.append(self.view.line(startpos[x].end()).end())
            for x in range(len(startpos))[1:]:
                endpos.append(self.view.line(startpos[x].end()).begin()-1)
            endpos.append(self.view.size())
            startpos=temp
        else:    
            for x in range(len(startpos)):
                startpos[x]=self.view.line(startpos[x].end()).end()

            endpos = self.view.find_all(endMarker)
            for x in range(len(startpos)):
                endpos[x]=self.view.line(endpos[x].begin()).begin() - 1

        for x in range( len(endpos)):
            content = sublime.Region(startpos[x], endpos[x])
            new_content=[content]
            if content.size() > 0:
                if self.view.fold(content) == False:
                    new_content = self.view.fold(content)
            self.selection = new_content

class UnfoldAllCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        s = sublime.load_settings('syntax_fold.sublime-settings')
        config=s.get('default')
        startMarker = config.get("startMarker")
        endMarker = config.get("endMarker")

        startpos = self.view.find_all(startMarker)
        endpos=[]
        if endMarker==None:
            temp=[]
            for x in range(len(startpos)):
                temp.append(self.view.line(startpos[x].end()).end())
            for x in range(len(startpos))[1:]:
                endpos.append(self.view.line(startpos[x].end()).begin()-1)
            endpos.append(self.view.size())
            startpos=temp
        else:    
            for x in range(len(startpos)):
                startpos[x]=self.view.line(startpos[x].end()).end()

            endpos = self.view.find_all(endMarker)
            for x in range(len(startpos)):
                endpos[x]=self.view.line(endpos[x].begin()).begin() 

        for x in range( len(endpos)):
            content = sublime.Region(startpos[x], endpos[x])
            new_content=[content]
            if content.size() > 0:
                new_content = self.view.unfold(content)
            self.selection = new_content

class FoldCurrentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        s = sublime.load_settings('syntax_fold.sublime-settings')
        config=s.get('default')
        startMarker = config.get("startMarker")
        endMarker = config.get("endMarker")
        sections = self.view.find_all(startMarker)
        sectionStart=[]
        sectionEnd=[]
        sectionLineEnd=[]
        for x in range(len(sections)):
            sectionStart.append(sections[x].begin())
            sectionEnd.append(sections[x].end())
            sectionLineEnd.append(self.view.line(sections[x].end()).end())

        endStart=[]
        endEnd=[]
        if endMarker==None:
            ends = sections[1:]
            for x in range(len(ends)):
                endStart.append(ends[x].begin()-1)
                endEnd.append(ends[x].end())
            endStart.append(self.view.size())
            endEnd.append(self.view.size())
        else:
            ends = self.view.find_all(endMarker)
            for x in range(len(ends)):
                endStart.append(ends[x].begin()-1)
                endEnd.append(ends[x].end())
            
        selection=self.view.sel()[0]
        for x in range(len(sectionStart)):
            if (sectionStart[x] < selection.begin()) and (endEnd[x] > selection.end()):
                content = sublime.Region(sectionLineEnd[x], endStart[x])
                new_content=[content]
                if content.size() > 0:
                    new_content = self.view.fold(content)
                self.selection = new_content

class UnfoldCurrentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        s = sublime.load_settings('syntax_fold.sublime-settings')
        config=s.get('default')
        startMarker = config.get("startMarker")
        endMarker = config.get("endMarker")
        sections = self.view.find_all(startMarker)
        sectionStart=[]
        sectionEnd=[]
        sectionLineEnd=[]
        for x in range(len(sections)):
            sectionStart.append(sections[x].begin())
            sectionEnd.append(sections[x].end())
            sectionLineEnd.append(self.view.line(sections[x].end()).end())

        endStart=[]
        endEnd=[]
        if endMarker==None:
            ends = sections[1:]
            for x in range(len(ends)):
                endStart.append(ends[x].begin()-1)
                endEnd.append(ends[x].end())
            endStart.append(self.view.size())
            endEnd.append(self.view.size())
        else:
            ends = self.view.find_all(endMarker)
            for x in range(len(ends)):
                endStart.append(ends[x].begin()-1)
                endEnd.append(ends[x].end())
        
        selection=self.view.sel()[0]
        for x in range(len(sectionStart)):
            if (sectionStart[x] < selection.begin()) and (endEnd[x] > selection.end()):
                content = sublime.Region(sectionLineEnd[x], endStart[x])
                new_content=[content]
                if content.size() > 0:
                    new_content = self.view.unfold(content)
                self.selection = new_content
