def printing_models(unprinted_designs, completed_models):

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        completed_models.append(current_design)

        print(f"\nprinting {current_design.title()}")

def printed_design(completed_models):

    print("\nThe following models have been printed")
    for completed_model in completed_models:
      
        print(completed_model.title())

designs = ["flier", "monogram", "Advertisement"]
completed_models = []
printing_models(designs, completed_models)

printed_design(completed_models)