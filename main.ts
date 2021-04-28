scene.onOverlapTile(SpriteKind.Player, sprites.builtin.forestTiles10, function (sprite, location) {
    game.over(true)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    game.over(false)
})
tiles.setTilemap(tilemap`level1`)
let myCorg = corgio.create(SpriteKind.Player)
myCorg.horizontalMovement()
myCorg.updateSprite()
myCorg.follow()
myCorg.verticalMovement()
let myEnemy = sprites.create(assets.image`myenemy`, SpriteKind.Enemy)
myEnemy.setPosition(100, 100)
forever(function () {
    myEnemy.setVelocity(16, 50)
})
