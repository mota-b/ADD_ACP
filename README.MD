##################
## Descriptions ##
##################
in this project we are going to reduce the number of dimention from our data-Mareix
with the less possible information loss;
in order to represente it in a plan (Better) or a 3D env (at less);

############
## Schema ##
############

MATRIX-data, dim(n*m), information(100%) ==> Reduce_Dim_Methode() ==> Representative(),dim(n*(2|3)), information(<100%)


- Methodes {
    ACP: "Analyse par Composent Principale"
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

        # find eigen vals "resove the equation : det(c - landa * I) = 0 " [every landa represent a % from our tota information]

        # find eigen vectors

        # calculate new axes witch represente our 5 variable
 
    else 
        # we can't apply acp      