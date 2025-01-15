class RoomNode:

    def __init__(self, room_name, cam_name):

        self.adjacent_rooms = {}
        self.name = room_name
        self.cam_name = cam_name



    def add_room(self, new_room):
        """ TODO: new_room should also append THIS room to its adjacent rooms list!!!!! """
        self.adjacent_rooms.append(new_room)
        new_room.adjacent_rooms.append(self)
