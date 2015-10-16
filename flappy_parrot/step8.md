**Step 7:** Add scoring {.activity}

The player should score a point every time Flappy makes it though a pipe. Let's add that next.

## Activity Checklist { .check}

+ Let's add a sound to play when Flappy scores a point. Click on the **Pipe** sprite add a score sound. **bird** is a good choice.
+ Now click back on the `Scripts` {.blockgrey} tab.
+ Make a new variable `For all sprites` {.blockgrey} and call it `score` {.blockorange}.
+ Add a block to set the score to 0 when the flag is clicked.
+ Add the following block:
```blocks
    when I start as a clone
        wait until <(x position) < ([x position v] of [Flappy v])>
        change [score v] by (1)
        play sound [bird v]
```

## Test Your Project { .flag}

__Click the green flag__, does the player score points for flying Flappy through the pipes?

## Save your project { .save}

## Things to try { .try}

+ __How many ways can you make this game easier or harder?__
+ __Well done you’ve finished the basic game. There are more things you can do to your game though. Have a go at these challenges!__

## Challenge 1: add a high score { .challenge}

+ Make a new variable and tick the `Cloud variable (stored on server)` {.blockgrey} box. Call the variable `hi-score` {.blockorange}
+ when the game is over check if you need to set a new high score:
```blocks
    when I receive [GameOver v]
        if <(score) > (hi-score)> then
            set [hi-score v] to (score)
        end
        stop [other scripts in sprite v]
```

## Test Your Project { .flag}

__Click the green flag__, does your score update the `hi-score`?

## Save your project { .save}

## Challenge 2: add gravity { .challenge}

When something falls under gravity it doesn't usually fall at a fixed rate. For this challenge we will make Flappy fall as if under gravity.

+ Add a new variable `For this sprite only` {.blockgrey} to **Flappy** and call it `rise` {.blockorange}.
+ Change Flappy's falling script:
```blocks
    when FLAG clicked
        set [rise v] to [0]
        go to x: (-50) y: (0)
        forever
            change y by (rise)
            change [rise v] by (-0.4)
```
+ And change Flappy's flapping script:
```blocks
    when FLAG clicked
        set [flaps v] to [0]
        switch costume to [wings up v]
        forever
            repeat until <(flaps) = [0]>
                change [flaps v] by (-1)
                switch costume to [wings down v]
                change [rise v] by (8)
                wait (0.2) secs
                switch costume to [wings up v]
                wait (0.2) secs
```

## Test Your Project { .flag}

__Click the green flag__, does Flappy now accelerate when falling and flapping?

## Save your project { .save}

## Challenge 3: fall off screen { .challenge}

When the player loses make Flappy fall off the bottom of the screen before ending the game.

+ Replace the `broadcast GameOver` {.blockbrown}  block with `broadcast Fall` {.blockbrown}
+ Now add the following scripts:
```blocks
    when I receive [Fall v]
        repeat (10)
            turn ccw (5) degrees

    when I receive [Fall v]
        repeat until <(y position) < [-180]>
            change y by (rise)
            change [rise v] by (-0.4)
        end
        hide
        broadcast [GameOver v]
```
+ Don't forget to add a `show` {.blockpurple} block and reset Flappy's direction when the game restarts.

## Test Your Project { .flag}

__Click the green flag__, does Flappy now fall off the screen after hitting a pipe? Does Flappy reappear in the correct orientation when restarting the game.

## Save your project { .save}

Well done, you’ve finished! Now you can enjoy your game!

Don’t forget you can share your game with all your friends and family by clicking on **Share** on the menu bar!
