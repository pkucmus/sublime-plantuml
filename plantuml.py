import os
from subprocess import PIPE, Popen

import sublime
import sublime_plugin


class PlantUmlCommand(sublime_plugin.TextCommand):

    def run(self, edit, *args):
        sublime.status_message('Processing PlantUML')
        self.view.set_status('plant', 'Processing PlantUML')
        content = self.view.substr(sublime.Region(0, self.view.size()))
        img_file_name = os.path.splitext(self.view.file_name())[0] + '.png'
        with open(img_file_name, 'w') as image_file:
            p = Popen(
                ['docker', 'run', '-i', '--rm', 'plantuml'],
                stdout=image_file, stdin=PIPE, stderr=PIPE
            )
            p.communicate(input=bytes(content, 'utf-8'))[0]
        self.view.window().open_file(img_file_name)
        self.view.window().focus_view(self.view)
        self.view.erase_status('plant')
        sublime.status_message()


class BehaveAutocomplete(sublime_plugin.EventListener):

    def is_uml(self, view):
        ext = os.path.splitext(view.file_name())[1]
        return ext == '.uml'

    def on_post_save_async(self, view):
        if self.is_uml(view):
            view.run_command('plant_uml')
