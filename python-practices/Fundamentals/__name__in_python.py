# UNDERSTANDING: __name__ == "__main__"

# 1. Python has no mandatory main() like Java. Python just runs the file
#    you pass to it, top to bottom. That file IS the entry point.

# 2. __name__ is a special variable Python sets AUTOMATICALLY for every file:
#       - python myfile.py   -> that file's __name__ == "__main__"
#       - import myfile       -> myfile's __name__ == "myfile"

# 3. Importing a module RUNS the whole file top to bottom. So any loose
#    print()/calls in it will fire on import (usually unwanted).

# 4. To avoid that, wrap run-only code in:
#       if __name__ == "__main__":
#    This block runs ONLY when the file is launched directly, NOT on import.

# 5. "main" is just a naming CONVENTION - Python gives the name no special
#    meaning. main() / start() / run() all behave the same.

# PROJECT STRUCTURE:
#   app.py  -> define a main() function (entry point) and call it inside
#              the if __name__ == "__main__": block, so it runs when launched
#              directly but stays silent when imported by another file.


if ___name___=="main" :
    print("hello world")