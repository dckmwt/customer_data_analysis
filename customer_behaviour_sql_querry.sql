     create database if not exists customer_behavior ;
     use customer_behavior ;

select * from cleaned_shopping_data limit 3900; 
     
	 --    Q.1 :- what is the total revenue genrated by male vs female customer 
      select gender , sum(purchase_amount) as total_revenue_by_gender_wise from  cleaned_shopping_data group by gender ;
      
       --    Q.2 :- which customer use discount but still spent more than the average purchase amount  
       select * from  cleaned_shopping_data where ( purchase_amount >=  (
        select avg(purchase_amount) from cleaned_shopping_data 
        ) AND discount_applied = "Yes"   );
     
      select * from cleaned_shopping_data where discount_applied = "Yes" ;
      
      --  Q.3 :- which are the top 5 products with the higest average review rating 

	select item_purchased , round(avg(review_rating) , 2) as avg_review_rating from cleaned_shopping_data group by item_purchased order by avg_review_rating desc limit 5 ;
	select category ,round(avg(review_rating) , 2) as avg_review_rating from cleaned_shopping_data group by category order by avg_review_rating desc ; 
    
    
    -- Q.4 :- compare the average purchase amount between standard and express shipping 
    
       select shipping_type , avg(purchase_amount) from cleaned_shopping_data where shipping_type in ("Standard" ,"Express") group by shipping_type;
	   select shipping_type , avg(purchase_amount) as avg_amount_by_shipping from cleaned_shopping_data  group by shipping_type order by avg_amount_by_shipping desc  ;
    
    --  Q.5 :- Do Subscribed customers spend more ? compare avergae spend and total revenue between subscribers and non-subscribers
    
          select subscription_status , count(customer_id) as total_customer ,
            avg(purchase_amount) as avg_spend , 
            sum(purchase_amount) as total_revenue 
            from cleaned_shopping_data group by subscription_status ;
    
    --  Q.6 :- which 5 products have the highest percentage of purchase with discount applied  
    
            select item_purchased , 
              round( sum(case when discount_applied = "Yes" then 1 else 0 end)/count(*) * 100.0 , 2 ) as discount_rate 
                from cleaned_shopping_data  
                group by item_purchased  
                order by discount_rate desc limit 5 ;
    
    --   Q.7 :- segment customer into new , returning , and loyal based on their total number of pervies purchase , and show the count of each segment 
    /*
    step1 :- with ki help se customer_type name ki ek temprarory table bnayenge 
            jisme customer_id , previous_purchases  ko liya gya hai 
    */
    
               with customer_type as (
               select customer_id , previous_purchases , 
               case 
                 when previous_purchases = 1 then "New" 
                  when previous_purchases between 2 and 10 then "Returning"
                  else "Loyal"
                  end as customer_segment 
                  from cleaned_shopping_data
               )  
       select customer_segment  , count(*) as "Number_of_customers" from customer_type group by customer_segment  ;
    
    --     Q.8 :- what are top 3 most purchased productes with in each category  

             with item_counts as (
             select category , item_purchased ,
             count(customer_id) as total_orders ,
             ROW_NUMBER() over (
             partition by category 
             order by count(customer_id) desc
             ) as item_rank
             from cleaned_shopping_data
             group by category , item_purchased
             )
    
       select  item_rank , category , item_purchased  , total_orders from item_counts ;
    
    
      --     Q.9 :- are customers who are repeat buyers (more than 5 previous purchase )  also likely to subscribe 
    
        select *  from  cleaned_shopping_data where  ( previous_purchases > 5  and subscription_status = "Yes") ;
    
       select subscription_status ,
       count(customer_id) as repeat_buyers
       from cleaned_shopping_data 
        where   previous_purchases > 5 
          group by subscription_status ;
        --  Q.10 :- what is the revenue contributation of each age group
       select age_group , sum(purchase_amount) as total_revenue_by_age_group 
       from  cleaned_shopping_data
       group by age_group 
       order by total_revenue_by_age_group desc ;
       
       select age_group , count(customer_id) as total_customer  from  cleaned_shopping_data group by age_group  ;