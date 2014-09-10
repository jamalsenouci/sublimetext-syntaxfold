import sublime, sublime_plugin

class FoldAllCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		
		sectionpos = self.view.find_all("'#Section")
		for x in range(len(sectionpos)):
			sectionpos[x]=self.view.line(sectionpos[x].end()).end()
		endpos = self.view.find_all("'#End")
		for x in range(len(sectionpos)):
			endpos[x]=self.view.line(endpos[x].begin()).begin() - 1
		
		for x in range( len(endpos)):
			content = sublime.Region(sectionpos[x], endpos[x])
			new_content=[content]
			if content.size() > 0:
				if self.view.fold(content) == False:
					new_content = self.view.fold(content)
			self.selection = new_content


class UnfoldAllCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		
		sectionpos = self.view.find_all("'#Section")
		for x in range(len(sectionpos)):
			sectionpos[x]=self.view.line(sectionpos[x].end()).end()
		
		endpos = self.view.find_all("'#End")
		for x in range(len(sectionpos)):
			endpos[x]=endpos[x].begin()

		for x in range( len(endpos)):
			content = sublime.Region(sectionpos[x], endpos[x])
			new_content=[content]
			if content.size() > 0:
				new_content = self.view.unfold(content)
			self.selection = new_content


class FoldCurrentCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sections = self.view.find_all("'#Section")
		sectionStart=[]
		sectionEnd=[]
		sectionLineEnd=[]
		for x in range(len(sections)):
			sectionStart.append(sections[x].begin())
			sectionEnd.append(sections[x].end())
			sectionLineEnd.append(self.view.line(sections[x].end()).end())

		endStart=[]
		endEnd=[]
		ends = self.view.find_all("'#End")
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
		sections = self.view.find_all("'#Section")
		sectionStart=[]
		sectionEnd=[]
		sectionLineEnd=[]
		for x in range(len(sections)):
			sectionStart.append(sections[x].begin())
			sectionEnd.append(sections[x].end())
			sectionLineEnd.append(self.view.line(sections[x].end()).end())

		endStart=[]
		endEnd=[]
		ends = self.view.find_all("'#End")
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
