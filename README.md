# pdfshrinker

Never stress out over `.pdf` submission file size limits again! Simply drag-n-drop your `.pdf` file (with all its glorious high-resolution graphics) onto the webpage hosted by this repository, and watch your `.pdf` file get magically shrunk to an appropriate filesize.

## How does it work?!

The power of friendship.  Also, `ghostscript`.  In particular, it runs:

```
gs -o out.pdf -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -dFastWebView=true -dColorImageResolution=500 -dGrayImageResolution=500 -dMonoImageResolution=500 -f in.pdf
```
For a more in-depth discussion of `ghostscript` options, check out [this documentation](http://ghostscript.com/doc/current/Ps2pdf.htm#Options).

## Live demosite

A [live demo site](https://pdfshrinker.davinci.cs.washington.edu/) is provided for academics panic-shrinking their `.pdf`s minutes before the deadline.  Note that although the proverbial hat has been tipped in the general direction of security, this service is provided as-is with no warranty, implied or otherwise.  I make no guarantees that those of you who upload stuff will get back nice `.pdf` files, or that the service is confidential.
