# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    # ...
    def mvmntobjbfld(self, field, x_unit, y_unit, direction, state_fly, state_crawl, points_per_action=1):
        if state_fly and state_crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if state_fly:
            points_per_action *= 1.2
            if direction == 'UP':
                new_y = y_unit + points_per_action
                new_x = x_unit
            elif direction == 'DOWN':
                new_y = y_unit - points_per_action
                new_x = x_unit
            elif direction == 'LEFT':
                new_y = y_unit
                new_x = x_unit - points_per_action
            elif direction == 'RIGHT':
                new_y = y_unit
                new_x = x_unit + points_per_action
        if state_crawl:
            points_per_action *= 0.5
            if direction == 'UP':
                new_y = y_unit + points_per_action
                new_x = x_unit
            elif direction == 'DOWN':
                new_y = y_unit - points_per_action
                new_x = x_unit
            elif direction == 'LEFT':
                new_y = y_unit
                new_x = x_unit - points_per_action
            elif direction == 'RIGHT':
                new_y = y_unit
                new_x = x_unit + points_per_action

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
