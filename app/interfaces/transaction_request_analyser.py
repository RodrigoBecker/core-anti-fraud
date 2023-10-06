from typing import Optional, List
from pydantic import BaseModel, Field


class Phone(BaseModel):
    phoneType: Optional[int]
    ddi: Optional[int]
    ddd: Optional[int]
    phoneNumber: Optional[str]


class Address(BaseModel):
    street: Optional[str]
    number: Optional[str]
    additionalInformation: Optional[str]
    district: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zipcode: Optional[str]
    contry: Optional[str]
    reference: Optional[str]
    neighborhood: Optional[str]


class Client(BaseModel):
    clientType: Optional[int]
    document: Optional[str]
    name: str
    birthDate: Optional[str]
    email: Optional[str]
    gender: Optional[str]


class BillingData(BaseModel):
    client: Client
    address: Address
    phones: List[Phone] = Field(default_factory=list)


class ShippingData(BaseModel):
    client: Client
    address: Address
    phones: List[Phone] = Field(default_factory=list)
    deliveryType: Optional[int]
    deliveryTime: Optional[str]
    shippingAmount: Optional[str]
    pickUpStoreDocument: Optional[str]


class Card(BaseModel):
    maskedPAN: Optional[str]
    hash: Optional[str]
    bin: Optional[str]
    end: Optional[str]
    brandCode: Optional[int]
    expirationMonth: Optional[int]
    expirationYear: Optional[int]
    cardholderName: str
    cardholderDocumentNumber: Optional[str]
    tid: Optional[str]


class PaymentData(BaseModel):
    paymentDateTime: Optional[str]
    amount: Optional[float]
    paymentMethod: Optional[int]
    installmentsQuantity: Optional[int]
    currency: Optional[int]
    card: Card
    address: Address


class Item(BaseModel):
    itemCode: Optional[str]
    itemName: Optional[str]
    amount: Optional[float]
    quantity: Optional[int]
    categoryCode: Optional[int]
    categoryName: Optional[int]
    isGift: bool
    isMarketPlace: bool
    sellerName: Optional[str]
    sellerDocument: Optional[str]
    courier: Optional[str]


class OrdemData(BaseModel):
    partnerOrderId: Optional[str]
    orderDateTime: Optional[str]
    relationshipType: Optional[str]
    amount: Optional[float]
    totalAmount: Optional[float]
    discountamount: Optional[int]
    ip: Optional[str]
    isGift: bool
    originChannel: Optional[str]
    businessId: Optional[int]
    MCC: Optional[int]
    SLA: Optional[int]
    items: List[Item] = Field(default_factory=list)


class TransactionRequestAnalyserInput(BaseModel):
    order: OrdemData
    billingData: BillingData
    shippingData: ShippingData
    paymentData: PaymentData


class TransactionRequestAnalyserOutput(BaseModel):
    ticket: Optional[str]
    date: Optional[str]
    message: str
