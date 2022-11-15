# ObtainingGradients

if you open this file, and scroll all the way down, you will see a line like this:
**Included Gradients: 80 QCIndex: 48**

for any study that we ran DTIPrep on, it creates a file called StudyID_QCReport.txt

is it possible to write a script so that the script will read the last time it says Included Gradients in this txt document and then put down the number next to it on a spreadsheet?

in this case it would be 80

so you would have one column which would be called "filename", and the other column called "last no of included gradients"

on for this example "filename" would be DWI_Abbott_003_QCReport.txt and "last no of included gradients" is 80

that last line of Included Gradients is not always going to be the same line in the txt file, for some people it might be a shorter txt file, for some people it might be a longer one. So you can't say "always read line number X" that will differ. But it is always the "last" line that says "included gradients"

and the first number next to it, not the QCIndex