##################
## Descriptions ##
##################
in this project we are going to reduce the number of dimention from our data-Mareix
with the less possible information loss;
in order to represente it in a plan (Better) or a 3D env (at less);

############
## Schema ##
############

MATRIX-data, dim(n*m), information(100%) ==> Reduce_Dim_Methode() ==> Matrix-Representative(),dim(n*(2|3)), information(<100%)


- Methodes {
    A.P.C: "Analyse by Principal Composent"
}


################
## Algorythme ##
################

    mat: matrix of data, dimention (m*n);
    mat_cen : centered matrix
    mat_R: reduced matrix

    # test if the matrix has quantitafi data
    if is_quantitafi(matrix) : # we can apply acp
        
        # center the matrix (on it's own gravity point)
        mat_cen = centered(mat)

        # reduce the matrix (the data has same echelle)
        mat_R = reduced(mat_cen)

        # corelation " var/var "
        C = (1/n) * transpose(mat_R) * mat_R

        # find eigen vals "resove the equation : det( transpose(mat_R) * mat_R - landa * I) = 0 " [every landa represent a % from our tota information]

        # find eigen vectors for all landa(s) "resove the equations : transpose(mat_R) * mat_R * V_i = landa_i * V_i "

        # calculate new axes witch represente our 5 variable
        exemple: Axe[i] = tuple(persone)_from_R * eigenVect[i]

        # calculate contribution of each persone in new axes 
        exemple: for each personne in Axe(i)
            weight(personne) =  ( 1/(nbr_personne) ) * ( valu_personne_in(Axe_i)²/eigenvalue(Axe_i) )
        
 
    else 
        # we can't apply acp      