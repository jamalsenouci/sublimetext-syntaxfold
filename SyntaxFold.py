import sublime, sublime_plugin


s = sublime.load_settings('syntax_fold.sublime-settings')
startMarker = s.get("startMarker")
endMarker = s.get("endMarker")

class FoldPanelCommand(sublime_plugin.TextCommand):
	self.panel_cache = []
	self.config_map = {}
	configs = s.get("prompt_config")
	for conf in configs:
		c=dict()
		c['start']=conf.get('start')
		c['end']=conf.get('end')
		self.panel_cache.append([conf['name']])
		self.config_map[conf['name']]=c
		
	self.view.window().show_quick_panel(self.panel_cache, self.on_done)
	
	def on_done(self, index):
		if index == -1:
			return
		name = self.panel_cache[index][0]
		self.view.run_command("fold", self.config_map[name])

class FoldCommand(sublime_plugin.TextCommand):
	def run(self, edit, all=True, prompt=False, unfold=False):
		if prompt:
			self.view.run_command("fold_panel")
		elif unfold:
			if all:
				self.view.run_command("unfold_all")
			else:
				self.view.run_command("unfold_current")
		else:
			if all:
				self.view.run_command("fold_all")
			else:
				self.view.run_command("fold_current")

class FoldAllCommand(sublime_plugin.TextCommand):
	def run(self, edit):	
		startpos = self.view.find_all(startMarker)
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
		startpos = self.view.find_all(startMarker)
		for x in range(len(startpos)):
			startpos[x]=self.view.line(startpos[x].end()).end()
		
		endpos = self.view.find_all(endMarker)
		for x in range(len(startpos)):
			endpos[x]=endpos[x].begin()

		for x in range( len(endpos)):
			content = sublime.Region(startpos[x], endpos[x])
			new_content=[content]
			if content.size() > 0:
				new_content = self.view.unfold(content)
			self.selection = new_content

class FoldCurrentCommand(sublime_plugin.TextCommand):
	def run(self, edit):
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
