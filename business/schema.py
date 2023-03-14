import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Business

class BusinessType(DjangoObjectType):
    class Meta:
        model = Business
        filter_fields = ['name', 'address','owner_name','website']
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    business = graphene.relay.Node.Field(BusinessType)
    all_businesses = DjangoFilterConnectionField(BusinessType)

class CreateBusiness(graphene.Mutation):
    class Arguments:
        # name, description, employee_size, address, phone_number, owner_name, owner_phone_number, website
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        employee_size = graphene.String(required=True)
        address = graphene.String(required=True)
        phone_number = graphene.String(required=True)
        owner_name = graphene.String(required=True)
        owner_phone_number = graphene.String(required=True)
        website = graphene.String(required=True)

    business = graphene.Field(BusinessType)

    def mutate(self, info, name, description, employee_size, address, phone_number, owner_name, owner_phone_number, website):
        business = Business(name=name, description=description, employee_size=employee_size, address=address, phone_number=phone_number, \
            owner_name=owner_name, owner_phone_number=owner_phone_number, website=website)
        business.save()
        return CreateBusiness(business=business)

class UpdateBusiness(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        description = graphene.String()
        employee_size = graphene.String()
        address = graphene.String()
        phone_number = graphene.String()
        owner_name = graphene.String()
        owner_phone_number  = graphene.String()
        website = graphene.String()

    business = graphene.Field(BusinessType)

    def mutate(self, info, id, name=None, description=None, address=None, phone_number=None,employee_size=None,owner_name=None,website=None):
        business = Business.objects.get(pk=id)
        if name:
            business.name = name
        if description:
            business.description = description
        if address:
            business.address = address
        if phone_number:
            business.phone_number = phone_number
        if employee_size:
            business.employee_size = employee_size
        if owner_name:
            business.owner_name = owner_name
        if website:
            business.website = website
        business.save()
        return UpdateBusiness(business=business)

class DeleteBusiness(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    business = graphene.Field(BusinessType)

    def mutate(self, info, id):
        business = Business.objects.get(pk=id)
        business.delete()
        return DeleteBusiness(business=business)

class Mutation(graphene.ObjectType):
    create_business = CreateBusiness.Field()
    update_business = UpdateBusiness.Field()
    delete_business = DeleteBusiness.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
