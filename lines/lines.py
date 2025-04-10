import sys

def main():

    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments ")
        
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments Not a Python file")
        
        elif (sys.argv[1])[-3:] != ".py": 
            sys.exit("Not a Python file")

        loc = []
        docstring = False
        with open(sys.argv[1]) as file:

            for line in file:
                line = line.strip()

                # multi-line
                if line.startswith(('"""', "'''")):
                    if line.endswith(('"""', "'''")) and len(line) > 6:
                        continue
                    docstring = not docstring
                    continue

                # Single comment
                if docstring or  line.startswith("#") or not line:
                    continue

                if line:
                    loc.append(line)

        print(len(loc))

    except FileNotFoundError:
        sys.exit("File Not Found")



if __name__== "__main__":
    main()