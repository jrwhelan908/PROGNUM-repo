{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7745047-59bd-4820-838c-68d2699c4f53",
   "metadata": {},
   "outputs": [],
   "source": [
    "D = float(input(\"Enter day: \"))\n",
    "M = float(input(\"Enter month: \"))\n",
    "Y = float(input(\"Enter year: \"))\n",
    "\n",
    "JD = 367*Y -7*(Y+((M+9)/12))/4 - 3*((Y+((M-9)/7))/100 + 1)/4 + (275*M)/9 + D + 17210289-0.5\n",
    "print(\"JD =\", J)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0bbcb2cb-30a6-4b94-bc81-4b91552b9425",
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
