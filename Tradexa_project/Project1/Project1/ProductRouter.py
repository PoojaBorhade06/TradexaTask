class ProductRouter:
    route_app_labels = {'Products'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'products'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'products'
        return None


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'products'
        return None























# class ProductRouter:
#     def db_for_read(self,model,**hints):
#         if model._meta.app_label=='Products':
#             return 'products'
#         return None
#
#     def db_for_write(self,model,**hints):
#         if model._meta.app_label=='Products':
#             return 'products'
#         return None
#
#     def allow_relation(self,obj1,obj2,**hints):
#         if obj1._meta.app_label=='Products' and obj2._meta.app_label=='Products':
#             return 'products'
#         return None
#
#     def allow_migrate(self,db,app_label,model_name=None,**hints):
#         if app_label=='Products':
#             return 'products'
#         return None