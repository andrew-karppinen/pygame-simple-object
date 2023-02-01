
#not used currently

def SetImage(self, image=None, object_size_x: int = None, object_size_y: int = None):
    if image != None:  # if image given
        self.image_ = image
        self.original_image_ = image  # used image rotation

        if object_size_y != None and object_size_x != None:  # if size given
            self.object_size_y_ = object_size_y
            self.object_size_x_ = object_size_x
        else:  # if size no given
            self.object_size_y_ = image.get_height()  # set object size to image size
            self.object_size_x_ = image.get_width()

    else:  # if image no given
        if object_size_y != None and object_size_x != None:  # if size given
            self.object_size_y_ = object_size_y
            self.object_size_x_ = object_size_x
        else:
            self.object_size_y_ = 1
            self.object_size_x_ = 1
