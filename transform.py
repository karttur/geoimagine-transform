'''
Created on 23 nov. 2018

@author: thomasgumbricht
'''


import shutil
#import geoimagine.gis.mj_gis_v80 as mj_gis 

class ProcessTransform:
    '''class for GDAL processing'''   
    def __init__(self, process, session, verbose):
        self.session = session
        self.verbose = verbose
        self.process = process


        for locus in self.process.srcLayerD:
            #print ('locus',locus)
            for datum in self.process.srcLayerD[locus]:
                #print ('    datum',datum)
                #print ('self.process.dstLayerD[locus][datum]',self.process.dstLayerD[locus][datum])
                for dstcomp in self.process.dstLayerD[locus][datum]:
                    if self.process.dstLayerD[locus][datum][dstcomp]._Exists() and not self.process.overwrite:
                        self.session._InsertLayer(self.process.dstLayerD[locus][datum][dstcomp], self.process.overwrite, self.process.delete)
                        print ('transform ready',self.process.dstLayerD[locus][datum][dstcomp].FPN)
                        continue 
                    for srccomp in self.process.srcLayerD[locus][datum]:
                        if not (self.process.srcLayerD[locus][datum][srccomp]):
                            print ('Src composition missing',datum)
                            continue
                        if self.process.proc.processid == 'MonthlyDayToMonthlyAncillary':
                            self._MonthlyDayToMonthly(locus,datum,srccomp,dstcomp)
                        else:
                            print (self.process.proc.processid)
                            NOTYER
                        self.session._InsertLayer(self.process.dstLayerD[locus][datum][dstcomp], self.process.overwrite, self.process.delete)

                    
                
    def _MonthlyDayToMonthly(self,locus,datum,srccomp,dstcomp):
        '''
        '''
        if self.process.params.inplace:
            NOTYES
        else:
            #copy layer while renaming
            shutil.copy(self.process.srcLayerD[locus][datum][srccomp].FPN, self.process.dstLayerD[locus][datum][dstcomp].FPN)             