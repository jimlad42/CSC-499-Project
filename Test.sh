#!/bin/bash
# A tester for the SortList script.
# (I have no idea what I'm doing, send halp)
echo "Sorting the list."
sudo python3 SortList.py
echo "Validating the sorted list."
if cmp -s SortedList.txt ForwardResult.txt
then
	echo "The list sorted forward properly."
else
	echo "The list didn't sort properly forward."
fi
sudo python3 SortList.py -r
echo "Validating the reversed list."
if cmp -s SortedList.txt ReverseResult.txt
then
        echo "The list reversed properly."
else
        echo "The list didn't reverse properly."
fi
