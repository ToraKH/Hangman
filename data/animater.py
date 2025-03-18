# import config as cng
# def animate(self, images):
#     """animates the pictures"""
#         #List of the poof images (in order)
#     self.poof_filenames = [cng.I0, cng.I1, cng.I2, cng.I3, cng.I4, cng.I5, cng.I6, cng.I7
#             , cng.I8]
    
#     self.current_image_index = 0
#     #Empty list for the scaled images
#     self.poof_images = []
#     #Load and convert each poof image accordinly
#     for filename in self.poof_filenames:
#         #Convert image to an alpha channel for rendering
#         image = pg.image.load(filename).convert_alpha()
#         #Add scaled images into the list
#         self.poof_images.append(image)

#         key = pg.key.get_pressed()
#         #Collect poof-images list
#         self.curr_poof_img = self.poof_images[self.current_image_index]
#         #Get dead player's position
#         poof_x = self.player.rect.x-(self.curr_poof_img.get_width()*0.35)
#         poof_y = self.player.rect.y-(self.curr_poof_img.get_height()*0.35)
#         #Draw images at player's position
#         self.screen.blit(self.curr_poof_img, (poof_x, poof_y)) 
#         if self.current_image_index >= 8:
#             self.current_image_index = 0
#         #Left
#         if key[pg.K_a]:
#             self.current_image_index.flip(image, True, False)
#             self.current_image_index += 1
#         #Righ
#         elif key[pg.K_d]:
#             self.current_image_index += 1
#         else:
#             while self.current_image_index >= 0:
#                 self.current_image_index += 1

            
