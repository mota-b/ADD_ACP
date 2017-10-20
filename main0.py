from Data import db
from Methodes import functions as fn, get_key as gt, menu as mn

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
def get_centered():
    print mat_centered

print bars
print variances
print sigmas
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
                    "list":[get_centered()]
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