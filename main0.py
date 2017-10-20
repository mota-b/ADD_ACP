from Data import db
from Methodes import functions as fn, get_key as gt, menu as mn
import numpy as np
import json

# Data
data = db.data
n = len(data['peopels'])
m = len(data['subjects'])

# Calculate Col's {moy, equart, sigma}
bars = fn.get_bars(data, n, m)
variances = fn.get_equartypes(data, bars, n, m)
sigmas = fn.get_sigmas(variances)

## Center 
mat_centered = fn.matrix_centre(data, bars, n ,m)
## Reduce
mat_reduced = fn.matrix_reduce(mat_centered, sigmas, n ,m)
## Corelation matrix
mat_corelation = ( float(1)/float(n) ) * np.dot(np.transpose(mat_reduced), mat_reduced)
## eigen values & eigen vectors
eigen = np.linalg.eigh(mat_corelation)
eigen_vals = np.flip(eigen[0], 0)
eigen_vects = np.flip(eigen[1], 0)
## weight of each eigen vals
weight_sum = np.array(fn.get_weights(eigen_vals) )


men = {
    "title": "Choose the methode", 
    "list": [
        {
            "title": "A.C.P",
            "isMen": True,
            "list": [ 
                {
                    "title": "Is quantitatif matrix ?",
                    "isMen": False,
                    "list":[fn.is_quantitatif()]
                },
                {
                    "title": "Centered matrix",
                    "isMen": False,
                    "list":[json.dumps(mat_centered.tolist())]
                },
                {
                    "title": "Reduced matrix",
                    "isMen": False,
                    "list":[json.dumps(mat_reduced.tolist())]
                },
                {
                    "title": "Corelation matrix (Var/Var)",
                    "isMen": False,
                    "list":[json.dumps(mat_corelation.tolist())]
                },
                {
                    "title": "Eigen Values & Vectors",
                    "isMen": True,
                    "list": [
                        {
                            "title": "Eigen Values",
                            "isMen": False,
                            "list":[json.dumps(eigen_vals.tolist())]    
                            
                        },
                        {
                            "title": "Eigen Vectors",
                            "isMen": False,
                            "list":[json.dumps(eigen_vects.tolist())]    
                            
                        },
                        {
                            "title": "Weight and cumulated weight of each eigen val",
                            "isMen": False,
                            "list":[json.dumps(weight_sum.tolist())]
                        },
                    ]
                }
            ]
        },
        {
            "title": "A.F.P",
            "isMen": False
        }
    ]
}

mn.menu(men)


#''' ,
#                            
                        
                        
#                        , , "Reduced matrix", "Corelation matrix (Var/Var)", "Eigen values && Eigen vectors", "New axes", "Return to Methodes menu (Q|q : to quite)"]
#                } 
#            }, 
#            "A_F_P", 
#            "Press (Q|q) to quite"
#            ]
#        },
#    "met_acp":{
#""        "title": "A.C.P steps",
#""        "list": ["Is quantitatif matrix ? ", "Centered matrix", "Reduced matrix", "Corelation matrix (Var/Var)", "Eigen values && Eigen vectors", "New axes", "Return to Methodes menu (Q|q : to quite)"],
#        "steps":[
#
#        ]

 #   }
#}
# '''
#
