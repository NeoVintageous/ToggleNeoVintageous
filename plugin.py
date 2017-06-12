import sublime
import sublime_plugin


class ToggleNeovintageous(sublime_plugin.ApplicationCommand):
    """A command that toggles the NeoVintageous plugin."""

    def run(self):
        settings = sublime.load_settings('Preferences.sublime-settings')
        ignored_packages = settings.get('ignored_packages', [])

        if 'NeoVintageous' in ignored_packages:
            ignored_packages.remove('NeoVintageous')
            status = 'enabled'
        else:
            ignored_packages.append('NeoVintageous')
            status = 'disabled'

        ignored_packages.sort()
        settings.set('ignored_packages', ignored_packages)
        sublime.save_settings('Preferences.sublime-settings')

        sublime.status_message('NeoVintageous is {}'.format(status))
