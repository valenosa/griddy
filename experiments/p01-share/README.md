# P-01 · Multi-photo share test

Throwaway page that resolves P-01 in the [model document](../../docs/model.md), section 10: does Instagram accept several images from the web share sheet as one Carousel, in order? Its result decides how F-06 and ADR-0003 continue. Experiments follow T-03 and are published by T-04 (SDD section 11).

## Open it

On the phone, in Chrome: <https://valenosa.github.io/griddy/experiments/p01-share/>

Web Share with files needs HTTPS and is not available on most desktop browsers, so opening the file locally only checks rendering and downloads.

## What it does

1. Prepares JPEGs at Export Quality (R-12): numbered test images, or the owner's photos center-cropped, at 1:1, 4:5 or 3:4 and `EXPORT_WIDTH_PX` wide.
2. Sends them three ways: all at once to the share sheet, one by one, or as numbered downloads (`01.jpg`, `02.jpg`…), the fallbacks listed in P-01.
3. Collects what the owner sees in Instagram and builds a report to paste back.

Test images carry a border and TOP/BOTTOM labels to spot extra cropping, and a dashed square showing what a 1:1 center crop would keep.

## Runs

| Run | Set | Action |
|---|---|---|
| 1 | 2 test images, 4:5 | Share all → Instagram Feed |
| 2 | 10 test images, 4:5 | Share all |
| 3 | 20 test images, 4:5 | Share all |
| 4 | 10 own photos, 4:5 | Share all |
| 5 | 10 test images, 1:1 and 3:4 | Share all |
| 6 | Only if runs 1 to 3 fail | Share one by one, then Download numbered files |

Copy the report after each run. Nothing is posted: stop at Instagram's editor.

## Result

Recorded in the model document (P-01) once the runs are done; this folder is then kept as a record or removed, per T-03.
