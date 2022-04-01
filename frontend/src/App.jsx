import React, { useRef, useEffect, useState } from "react"

import { disableBodyScroll } from "body-scroll-lock"

import { Box, Paper, BottomNavigation, BottomNavigationAction } from "@mui/material"
import { Restore, Favorite, LocationOn } from "@mui/icons-material"

const App = () => {
    const lock = useRef(null)
    const [value, setValue] = useState(0)

    useEffect(() => {
        disableBodyScroll(lock.current)
    })

    return (
        <Box>
            <Paper
                sx={{ position: "fixed", top: 0, left: 0, right: 0 }}
                elevation={3}
                ref={lock}
            >
                <BottomNavigation
                    value={value}
                    onChange={(event, newValue) => {
                        setValue(newValue)
                    }}
                >
                    <BottomNavigationAction label="Recents" icon={<Restore />} />
                    <BottomNavigationAction label="Favorites" icon={<Favorite />} />
                    <BottomNavigationAction label="Nearby" icon={<LocationOn />} />
                </BottomNavigation>
            </Paper>
        </Box>
    )
}

export default App
