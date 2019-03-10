# Bash

# aliases

```bash
# open iTerm
alias iterm="open . -a iTerm"
```

# functions

Use [bashdoc](https://github.com/ajdiaz/bashdoc) to generate documentation.

```bash
# List C Functions
# fun: list-c-functions filename.c
#      helpful when factoring to header file
#      or moving functions under main
# txt: extract function declarations
# opt: filename: the c file to be scanned
# use: list-c-functions main.c
function list-c-functions () {
  grep -oE "^\w+ \S+\(.+)" "$1" | # get function definitions
  sort -u                       | # weed out duplicates (because of existing declarations)
  grep -v "int main("           | # remove the main declaration
  while read LINE; do             # add `;` to the end of each line
    echo $LINE\;;
  done
}

# Simple Image Converter
# fun: sic from to [images...]
# txt: convert images and rename file
#      and extension accordingly
# opt: from     : format to be converted from
# opt: to       : format to be converted to
# opt: images...: images to convert
# use: sic png jpeg *.png
function sic () {
  from="$1"; shift
  to="$1"  ; shift
  for i in $@; do
    sips -s format $to $i --out "${i%$from}$to";
  done
}

# Wrapper for ngrok
# fun: egrok port
# txt: shortcut for http port forwarding with ngrok.
# opt: port : for to forward with ngrok
# use: egrok 8080
function egrok () {
  ngrok http "$1" -host-header="localhost:$1"
}
```
