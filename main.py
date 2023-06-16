from scale import Scale


# input [note, scale(major,minor)]
starting_note=input("Choose your starting note:\n")
scale_method=input("Choose your scale:\n")

scales = {
    #major
    "major" : (2,2,1,2,2,2,1),

    #minor
    "minor" : (2,1,2,2,1,2,2,)
}

scale_method = scales[scale_method]

scale = Scale(scale_method)

scale.genarate_scale(starting_note=starting_note)

