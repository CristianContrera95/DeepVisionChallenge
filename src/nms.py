"""
__author__ = Cristian Contrera
__email__ = cristiancontrera95@gmail.com
__date__ = 15/10/2019
"""


import numpy as np


def nms(boxes, overlapThresh):
    """
    :param boxes: array of tuples like (x,y,w,h)
    :param overlapThresh: float used to represent overlap percentage
    """
    if len(boxes) <= 0:
        return []
    
    # get the coordinates of the all bounding boxes
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = x1 + boxes[:, 2]
    y2 = y1 + boxes[:, 3]

    # compute the area of the boxes and sort the boxes by the bottom-right y-coordinate
    area = (x2 - x1+1) * (y2 - y1+1)
    idxs = np.argsort(y2)

    pick = []
    while len(idxs) > 0:

        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)
        suppress = [last]

        # loop over all indexes in the indexes list
        for pos in range(last):
            j = idxs[pos]

            # find the largest (x, y) coordinates for the top-left of the boxes and
            # the smallest (x, y) coordinates for the bottom-right of the boxes
            xx1 = max(x1[i], x1[j])
            yy1 = max(y1[i], y1[j])
            xx2 = min(x2[i], x2[j])
            yy2 = min(y2[i], y2[j])

            # compute the width and height of the box
            w = max(0, xx2 - xx1 + 1)
            h = max(0, yy2 - yy1 + 1)

            # compute the ratio of overlap between the computed box and the box in the area list
            overlap = float(w * h) / area[j]

            if overlap > overlapThresh:
                suppress.append(pos)

        idxs = np.delete(idxs, suppress)

    return boxes[pick]