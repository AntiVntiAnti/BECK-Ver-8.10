model_setup = {
    "model_name": "tableview_name",
}

for model, table in model_setup.items():
    print(f"""self.{model} = create_and_set_model(
        {table},
        self.{table}view"""
    )
