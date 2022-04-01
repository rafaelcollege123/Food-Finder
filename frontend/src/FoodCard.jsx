import { Card, CardMedia } from "@mui/material"
import React from "react"
import TinderCard from "react-tinder-card"
import "./App.css"

const FoodCard = () => {
    const food = [
        {
            name: "Pizza",
            url: "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-keto-pizza-073-1544039876.jpg",
        },
        {
            name: "Ramen",
            url: "http://cdn.shopify.com/s/files/1/0111/1729/7722/articles/shutterstock_697241275_tonkotsu_ramen-landscape.jpg?v=1562316760",
        },
        {
            name: "Steak",
            url: "https://www.cookingclassy.com/wp-content/uploads/2019/07/steak-marinade-12.jpg",
        },
    ]
    return (
        <div>
            <div className="foodCard__container">
                {food.map((dish) => (
                    <TinderCard className="swipe" key={dish.name}>
                        <Card sx={{ height: "50vh" }}>
                            <CardMedia
                                component="img"
                                image={dish.url}
                                width="100%"
                                height="100%"
                            />
                        </Card>
                    </TinderCard>
                ))}
            </div>
        </div>
    )
}

export default FoodCard
