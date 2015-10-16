**Step 2:** Make Flappy fly {.activity}

Next, we want Flappy to flap upwards when you press the space bar.

## Activity Checklist { .check}

+ Click on the __Costumes__ tab and name the costumes **wings up** and **wings down**.
+ Now switch back to the __Scripts__ tab and add this script:
```blocks
    when [space v] key pressed
        switch costume to [wings down v]
        repeat (10)
            change y by (6)
        end
        switch costume to [wings up v]
        repeat (10)
            change y by (6)
        end
```

## Test Your Project { .flag}

__Click the green flag__, are you able to control Flappy with the space bar? Do you notice that sometimes you press the space bar but Flappy doesn't move? We'll fix that next...

## Save your project { .save }
