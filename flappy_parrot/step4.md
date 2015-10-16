**Step 3:** Fix the controls {.activity .new-page }

We'd like Flappy to respond every time we press the space bar. But when we push the space bar Flappy begins two loops of movements. If we push the space bar again before these loops have finished, Scratch ignores the second press. To solve this, we'll use a variable to count up how many flaps we need to do.

## Activity Checklist { .check}

+ Disconnect the blocks under the `when space key pressed` {.blockbrown} and put them to the side (we'll use them in a few moments.)
+ Make a new variable `For this sprite only` {.blockgrey} and call it `flaps` {.blockorange}.
+ Add the following script by draging in the blocks you put aside:
```blocks
    when FLAG clicked
        set [flaps v] to [0]
        switch costume to [wings up v]
        forever
            repeat until <(flaps) = [0]>
                change [flaps v] by (-1)
                switch costume to [wings down v]
                repeat (10)
                    change y by (6)
                end
                switch costume to [wings up v]
                repeat (10)
                    change y by (6)
                end
```
+ Finally, add to your `when space key pressed` {.blockbrown} event:
```blocks
    when [space v] key pressed
        change [flaps v] by (1)
```

## Test Your Project { .flag}

__Click the green flag__, does Flappy now flap once for each time you press the space bar?

## Save your project { .save}
