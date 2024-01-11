#include "lists.h"

/**
 * print_dlistint - prints all the elements of a dlistint_t list.
 * @h: pointer to the list.
 * Return: number of nodes.
 **/
size_t print_dlistint(const dlistint_t *h)
{
    size_t i = 0;
    const dlistint_t *L = h;

    while (L != NULL)
    {
        printf("%i\n", L->data);
        i++;
        L = L->next;
    }
    return (i);
}