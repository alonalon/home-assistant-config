from enum import Enum

"""
Global definitions that are used everywhere in my automations for easy access

"""

presence_state = {}
# Change this if you want to change the display name
presence_state["home"] = "Home"
presence_state["just_arrived"] = "Just arrived"
presence_state["just_left"] = "Just left"
presence_state["away"] = "Away"
presence_state["extended_away"] = "Extended away"

PEOPLE = {
    'Aron': {
        'device_tracker': 'person.aron',
        'proximity': 'proximity.prox_home_aron',
        'notifiers': ['ah']
    }
}

class GlobalEvents(Enum):
    """
        Add global events that are shared between componets
    """