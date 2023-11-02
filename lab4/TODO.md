1. Test with different features (or combination of features):

	1.1. Test with features = [Price,Open,High,Low]

	1.2  Or 1: Price_mean = (Price+Open+High+Low)

1. Test with more models (2-3):
	- https://scikit-learn.org/stable/supervised_learning.html

1. Use cross_validation:
	https://nbviewer.org/github/geekcourses/JupyterNotebooksExamples/blob/master/Notebooks/model_evaluation_and_optimization/cross_validation_full.ipynb

1. Create a function to fit and evaluate a models

	def evaluate_model(model, X_train, y_train):

		#Create linear regression object and train the model
		model = model().fit(X_train, y_train)

		# Estimate model:
		mae = mean_absolute_error(y_test,y_pred)
		print("MAE for <model_name>: %.2f"%mae )


	models = [LinearRegression, LogisticRegression]

	for model in models:
		evaluate_model(model, X_train, y_train)


