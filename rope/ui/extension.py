"""rope extension module

This module contains interfaces and instructions for extending rope
actions.

"""


class Action(object):
    """Extending rope commands

    Represents an action that can have keyboard a short-cut and
    menu item.  The `do` method is called when the action is
    invoked.  `Action`\s should be registered using `rope.ui.core.
    Core.register_action` method.  Usually `Action`\s are registered
    using `rope.ui.core.Core._load_actions` by loading the modules
    that register their actions when loading.

    """

    def get_name(self):
        """Return the name of this action.

        It might be useful when changing default keybindings.
        """

    def do(self, context):
        """Perform the action.

        `context` parameter is an `ActionContext` instance.
        """

    def get_menu(self):
        """Returns a `rope.ui.menubar.MenuAddress` or `None`."""

    def get_default_key(self):
        """Returns the keybinding for this action or `None`

        The result should be a string that indicates key sequence in
        emacs style.  Like 'C-x C-f' or 'M-X'.
        """

    def get_active_contexts(self):
        """Return a list of context names this actions is active in

        The list can contain 'python', 'rst', 'others', 'all' or
        'none'.  'none' context is active when no editor is open.
        """


class ActionContext(object):

    def __init__(self, core):
        self.core = core

    def get_core(self):
        return self.core

    def get_active_editor(self):
        return self.core.get_editor_manager().active_editor

    def _get_open_project(self):
        return self.get_core().get_open_project()

    def _get_active_editor_resource(self):
        return self.get_active_editor().get_file()

    def _get_active_editor_editor(self):
        return self.get_active_editor().get_editor()

    def _get_editing_context(self):
        return self.get_active_editor().get_editor().get_editing_context().editingtools

    def _get_buffer_offset(self):
        return self.editor.get_current_offset()

    project = property(_get_open_project)
    fileeditor = property(get_active_editor)
    editor = property(_get_active_editor_editor)
    offset = property(_get_buffer_offset)
    resource = property(_get_active_editor_resource)
    editingtools = property(_get_editing_context)


class SimpleAction(Action):
    """A simple `Action`"""

    def __init__(self, name, command, default_key=None, menu_address=None,
                 active_contexts=['all', 'none']):
        self.name = name
        self.command = command
        self.key = default_key
        self.menu = menu_address
        self.active_contexts = active_contexts

    def get_name(self):
        return self.name

    def do(self, context):
        self.command(context)

    def get_menu(self):
        return self.menu

    def get_default_key(self):
        return self.key

    def get_active_contexts(self):
        return self.active_contexts
