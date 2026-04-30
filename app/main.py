class CarWashStation:
    ...

    def serve_cars(self, cars: List[Car]) -> float:
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, new_rating: int) -> None:
        total_rating_sum = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(
            (total_rating_sum + new_rating) / self.count_of_ratings,
            1
        )
