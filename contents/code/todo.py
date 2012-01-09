# -*- coding: iso-8859-1 -*-
import commands
import sys
import re

class TodoItem():
	_priority = ""
	_number = ""
	_text = ""
	_rawtext = ""
	_contexts = list()
	_projects = list()
	def __init__(self, number, raw_text):
		self._rawtext = raw_text
		self._contexts = list()
		self._projects = list()
		self._number = number
		words = raw_text.split(" ")
		
		pri_match = ""
		proj_match = ""
		cont_match = ""
		i = 0
		for word in words:
			i += 1
			pri_match = re.search("\(([A-Z])\)", word)
			proj_match = re.search("\+(\w+)", word)
			cont_match = re.search("@(\w+)", word)
			if ( (i == 1) and (pri_match != None) ):
					self._priority =  pri_match.group(1)
			elif ( proj_match != None ):
				self._projects.append(proj_match.group(1))
			elif ( cont_match != None ):
				self._contexts.append(cont_match.group(1))
			else:	
				self._text += word + " "
	def getPriority(self):
		return self._priority
	
	def getNumber(self):
		return self._number
	
	def getContexts(self):
		return self._contexts
	
	def getProjects(self):
		return self._projects
	
	def getRaw(self):
		#raw_text = self._number + " (" + self._priority + ") " + self._text
		#return raw_text
		return self._number + " " + self._rawtext
	
	def getText(self,number=False,priority=False,projects=False,contexts=False):
		text = ""
		if number == True:
			text = text + self._number + " "
		if priority == True:
			if self._priority != "":
				text = text + "(" + self._priority + ") " 
		text = text + self._text
		if projects == True:
			for project in self._projects:
				text = text + "+" + project + " "
		if contexts == True:
			for context in self._contexts:
				text = text + "@" + context + " "
		return text
	

class TodoList():
	_todos = list()
	_todos_sorted = list()
	_binPath = ""
	_dataPath = ""
	_colors = dict()
	
	def __init__(self, data_path):
		self._dataPath = data_path
		self.refreshList()
	
	def setDataPath(self, data_path):
		self._dataPath = data_path
	
	def refreshList(self):
		try:
			f = open(self._dataPath)
			lines = f.readlines()
			f.close
		except IOError:
			print "Error: unable to read ", self._dataPath
			sys.exit()
		else:
			self._todos = list()
			i = 1 
			for line in lines:
				(text, junk) = line.split("\n")
				todo = TodoItem(str(i), text)
				self._todos.append(todo)
				i += 1
	
	def getList(self):
		return self._todos
	
	def sortList(self):
		return self.mergeSort(self._todos)
	
	def mergeSort(self, l):
		if len(l) < 2:
		  return l 
		else:
		  # recursively sort 
		  middle = len(l) / 2
		  # sorting left size
		  left = self.mergeSort(l[:middle])
		  right= self.mergeSort(l[middle:])
		  return self.merge(left,right)
	def merge(self, left, right):
		# merge the left list with the right list and return the result
		result = list()
		i,j = 0,0
		while i < len(left) and j < len(right):
		  if (left[i].getPriority() != "" and left[i].getPriority() <= right[j].getPriority()) or right[j].getPriority() == "":
		    result.append(left[i])
		    i += 1
		  else:
		    result.append(right[j])
		    j += 1
		result += left[i:]
		result += right[j:]
		return result
		
	def getListHTML(self):
		for todo in self._todos:
			text = "<span style=\"" + self._colors( todo.getPriority() ) + "\">" + todo.getText()  + "</span>\n"
			output.append(text)
		return output

