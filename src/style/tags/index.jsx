import { styled } from "styled-components"
import { Link } from "react-router-dom"

export const Div = styled.div`
    display: ${props => props.$flex == true ? "flex" : ""};
    gap: ${props => props.gap};
    flex-direction: ${props => props.direction};
    margin-bottom: ${props => props.bottom};
    margin-top: ${props => props.top};
    justify-content: center;
    align-items: center;
`

export const Title = styled.h1`
    font-size: ${props => props.fontSize};
`

export const Description = styled.p`
    font-size: ${props => props.fontSize};
    display: ${props => props.display || ""};
`

export const TitleLink = styled.h3`
    font-size: ${props => props.fontSize};
    cursor: pointer;
`

export const LinkRouter = styled(Link)`
    display: ${props => props.$flex == true ? "flex" : ""};
    background-color: ${props => props.back};
    padding: ${props => props.padding || ".3rem"};
    font-size: ${props => props.fontSize};
    border-radius: 6px;
    color: #000;
    align-items: center;
    justify-content: start;
    width: auto;
    gap: .3rem;
`

export const Span = styled.span`
    font-size: ${props => props.fontSize};
    display: ${props => props.$flex == true ? "flex" : ""};
    margin: ${props => props.margin};
`