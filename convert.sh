#!/bin/bash

CONV="../pdfminer-20140328/tools/pdf2txt.py"

for pdf in `ls data/*.pdf`; do
    filename=$(basename $pdf)
    filename="${filename%.*}"
    echo "Convert $pdf to html"
    $CONV -o "html/$filename.html" -c utf8 $pdf
done
