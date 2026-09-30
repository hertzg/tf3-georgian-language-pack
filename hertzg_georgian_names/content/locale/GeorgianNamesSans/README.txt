Georgian Names Sans is Lato with the Georgian letters of Noto Sans Georgian
added, scaled to Lato's x-height. It is renamed because Lato's license
reserves the name "Lato" for unmodified versions. Both source fonts are
licensed under the SIL Open Font License 1.1; see the OFL-*.txt files.

The Georgian letters come from the variable Noto Sans Georgian, scaled to 80%
of Lato's x-height (they read larger than Latin at equal x-height), at weights
chosen so their strokes still match Lato after scaling, about 5% lighter:

  Lato Light   <- wght 310
  Lato Regular <- wght 525
  Lato Medium  <- wght 580
  Lato Bold    <- wght 720

Rebuild with tools/merge_fonts.py <lato> <noto instance> <out> "Georgian Names Sans" <style> 0.80
