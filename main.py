def on_overlap_tile(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.builtin.forest_tiles10,
    on_overlap_tile)

def on_on_overlap(sprite, otherSprite):
    game.over(False)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

tiles.set_tilemap(tilemap("""
    level1
"""))
myCorg = corgio.create(SpriteKind.player)
myCorg.horizontal_movement()
myCorg.update_sprite()
myCorg.follow()
myCorg.vertical_movement()
myEnemy = sprites.create(assets.image("""
    myenemy
"""), SpriteKind.enemy)
myEnemy.set_position(100, 100)

def on_forever():
    myEnemy.set_velocity(16, 50)
forever(on_forever)
