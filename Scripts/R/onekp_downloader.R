library('onekp')
onekp <- retrieve_onekp()
peps <- filter_by_species(onekp, 'Pinus radiata')
download_peptides(peps,'Onekp/peps')
