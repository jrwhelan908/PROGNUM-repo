{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9625505f-41a8-4c41-a0c6-a1e9bcbcecf6",
   "metadata": {
    "tags": [
     "homework"
    ]
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "a = 1\n",
      "b = 0\n",
      "c = -1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Two solutions: x1 = 1.0 and x2 = -1.0\n"
     ]
    }
   ],
   "source": [
    "from math import sqrt\n",
    "\n",
    "a = float(input(\"a =\"))\n",
    "b = float(input(\"b =\"))\n",
    "c = float(input(\"c =\"))\n",
    "\n",
    "D = b**2 -4*a*c\n",
    "\n",
    "if D>0:\n",
    "    x1 = (-b+(sqrt(D))/(2*a))\n",
    "    x2 = (-b-(sqrt(D))/(2*a))\n",
    "    print(f\"Two solutions: x1 = {x1} and x2 = {x2}\")\n",
    "    \n",
    "elif D==0:\n",
    "    x = (-b/(2*a))\n",
    "    print(f\"One solution: x = {x}\")\n",
    "    \n",
    "else:\n",
    "    print(\"No real solutions\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8864e51c-2238-416a-9e66-558576bf7fde",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
