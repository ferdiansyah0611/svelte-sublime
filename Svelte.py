import sublime
import sublime_plugin
from .completion import html_svelte, js_svelte, non_svelte

class SvelteCommand(sublime_plugin.EventListener):
	
	def on_query_completions(self, view, prefix, locations):
		target = html_svelte
		is_svelte = view.match_selector(locations[0], "text.html.svelte")
		is_js = view.match_selector(locations[0], "source.js")

		if is_svelte == False and is_js == False: return []
		if is_js: target = non_svelte

		prefix 	= prefix.lower()
		out 	= []
		cursor 	= locations[0] - len(prefix) - 1
		line   	= view.substr(sublime.Region(0, cursor))
		split  	= line.split('\n')

		if is_svelte:
			is_html = '</script>' in split
			if is_html == False:
				target = js_svelte

		for comp in target:
			if comp.trigger.startswith(prefix):
				out.append(comp)

		return out