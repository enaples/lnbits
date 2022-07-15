async def m001_initial(db):
    """
    Initial products table.
    """
    await db.execute(
        """
        CREATE TABLE diagonalley.products (
            id TEXT PRIMARY KEY,
            stall TEXT NOT NULL,
            product TEXT NOT NULL,
            categories TEXT,
            description TEXT,
            image TEXT,
            price INTEGER NOT NULL,
            quantity INTEGER NOT NULL
        );
    """
    )

    """
    Initial stalls table.
    """
    await db.execute(
        """
        CREATE TABLE diagonalley.stalls (
            id TEXT PRIMARY KEY,
            wallet TEXT NOT NULL,
            name TEXT NOT NULL,
            publickey TEXT,
            privatekey TEXT,
            relays TEXT,
            shippingzones TEXT NOT NULL
        );
    """
    )

    """
    Initial zones table.
    """
    await db.execute(
        """
        CREATE TABLE diagonalley.zones (
            id TEXT PRIMARY KEY,
            "user" TEXT NOT NULL,
            cost TEXT NOT NULL,
            countries TEXT NOT NULL
        );
    """
    )

    """
    Initial orders table.
    """
    await db.execute(
        """
        CREATE TABLE diagonalley.orders (
            id TEXT PRIMARY KEY,
            productid TEXT NOT NULL,
            usr TEXT NOT NULL,
            pubkey TEXT NOT NULL,
            product TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            shippingzone INTEGER NOT NULL,
            address TEXT NOT NULL,
            email TEXT NOT NULL,
            invoiceid TEXT NOT NULL,
            paid BOOLEAN NOT NULL,
            shipped BOOLEAN NOT NULL,
            time TIMESTAMP NOT NULL DEFAULT """
        + db.timestamp_now
        + """
        );
    """
    )
