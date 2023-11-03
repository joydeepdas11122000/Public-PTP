import psychrolib
import psychrolib as pl

pl.SetUnitSystem(psychrolib.SI)
P = 101325

# https://psychrometrics.github.io/psychrolib/api_docs.html

print(pl.GetTKelvinFromTCelsius(100))
