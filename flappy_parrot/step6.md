**Step 5:** Make the pipes move {.activity}

Next we'll make the pipes move and arrange them randomly to provide an obstacle course for Flappy.

## Activity Checklist { .check}

+ Click on your **Pipe** sprite and select the `Scripts` {.blockgrey} tab.
+ Add the following scripts:
```blocks
    when FLAG clicked
        hide
        set size to (200)%
        forever
            create clone of [myself v]
            wait (2) secs

    when I start as a clone
        go to x: (240) y: (pick random (-80) to (80))
        show
        repeat (120)
            change x by (-4)
        end
        delete this clone
```

## Test Your Project { .flag}

__Click the green flag__, do pipes appear with gaps to fly through at different heights? If you find it difficult to navigate Flappy through the pipes without touching them, you can make the gap bigger in the **pipe** sprite by editing the costume.

## Save your project { .save}
