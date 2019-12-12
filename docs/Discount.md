# Discount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of discount. Will be used as order line text. | 
**description** | **str** | Optional description of discount | [optional] 
**amount** | **int** | Fixed amount discount deducted from order line amounts including VAT | [optional] 
**percentage** | **int** | Percentage discount applied to each applicable order line | [optional] 
**handle** | **str** | Per account unique handle for the discount | 
**state** | **str** | Discount state &#x60;active&#x60; or &#x60;deleted&#x60;. | 
**deleted** | **datetime** | Date when the discount was deleted if deleted. In ISO-8601 extended offset date-time format. | [optional] 
**created** | **datetime** | Date when the discount was created. In ISO-8601 extended offset date-time format. | 
**apply_to** | **list[str]** | Which order lines the discount is applicable to: &#x60;all&#x60;, &#x60;setup_fee&#x60;, &#x60;plan&#x60;, &#x60;additional_cost&#x60;, &#x60;add_on&#x60; and &#x60;ondemand&#x60; | 
**fixed_count** | **int** | Apply discount to a fixed number of invoices | [optional] 
**fixed_period_unit** | **str** | Time unit use for fixed valid period either &#x60;days&#x60; or &#x60;months&#x60; | [optional] 
**fixed_period** | **int** | Fixed period length e.g. 12 months or 14 days | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


