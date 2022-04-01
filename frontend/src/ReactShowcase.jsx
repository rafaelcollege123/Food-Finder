import React, { useState } from "react"
import { Typography, Container, Button } from "@mui/material"

const ReactShowcase = () => {
    const [count, setCount] = useState(0)

    const updateCount = () => {
        setCount(count + 1)
    }

    return (
        <Container maxWidth="sm">
            <Typography variant="h2" gutterBottom>
                React + Vite + MUI
            </Typography>
            <Typography variant="body1" gutterBottom>
                MUI provides a robust, customizable, and accessible library of
                foundational and advanced components, enabling you to build your own
                design system and develop React applications faster. Hello world
            </Typography>

            <Button variant="contained" onClick={updateCount}>
                Count: {count}
            </Button>
        </Container>
    )
}

export default ReactShowcase
