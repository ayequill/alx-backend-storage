-- Creates a trigger to handle an event where a new order is added
-- the trigger decreases the quantity of the order
CREATE TRIGGER after_insert_order
    AFTER INSERT ON orders FOR EACH ROW
    BEGIN
        UPDATE items
        SET quantity = quantity - NEW.number
        WHERE name = NEW.item_name;
    END;
